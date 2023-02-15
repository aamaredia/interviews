class MarkdownReader(object):
  """
  Iterator to traverse lines of Markdown
  """
  def __init__(self, text):
    self.text = text
    self.lines = text.split('\n')
    self.index = 0

  def rewind(self, count=1):
    """
    Look back at the previous line
    """
    return self.lines[self.index - count]
  
  def peek(self, count=0):
    """
    Look at the next line, but don't increment the index
    """
    # The index is always on the next item, hence
    # why this is going to default to 0
    return self.lines[self.index + count]

  def increment(self, count=1):
    """
    Moves the index by the specified count
    """
    self.index += count

  def __iter__(self):
    return self

  def __next__(self):
    try:
      item = self.lines[self.index]
    except IndexError:
      raise StopIteration()
    else:
      self.index += 1
      return item
  
class MarkdownParser(object):
  """
  Converts markdown text into HTML

  Note: Markdown text is new line deliminated
  """
  @classmethod
  def html_tag_text(cls, tag, text):
    """
    Brackets some text with the given html tag 
    """
    return f'<{tag}>{text}</{tag}>'

  @classmethod
  def parse_line(cls, line):
    """
    Vaguely named function that returns the html tag
    of the line if there is one and the text and the
    text without markdown tokens
    """
    split_lines = line.split()
    if not split_lines:
      return None, line
      
    potential_token = split_lines[0]

    if potential_token.startswith('#'):
      token_length = len(potential_token)
      return f'h{token_length}', line[token_length + 1:]
    elif potential_token.startswith('*'):
      return 'li', line[2:]
    else:
      return 'p', line

  @classmethod
  def traverse_ahead(cls, reader, token):
    """
    Generator that traverses ahead through the reader 
    and yields lines if the token matches the passed token

    Increments the reader as it does so
    """
    while True:
      try:
        next_token, next_text = cls.parse_line(reader.peek())
      except IndexError:
        break
      if next_token == token:
        reader.increment()
        yield next_token, next_text
      else:
        return
      
  @classmethod
  def to_html(cls, text):
    """
    Converts given string from markdown to html
    Implemented as a classmethod cause I hate instanciating
    needless objects. Could support both with some quick
    changes and what not, but keeping this simple and a 
    bit silly for now
    """
    html_out = []

    # MarkdownReader is used to move thru lines as we
    # sometimes increment within the loop when processing
    # certain tokens (lists, line breaks)
    reader = MarkdownReader(text)
    for line in reader:
      token, clean_text = cls.parse_line(line)
      
      if not token:
        # Empty line, carry on
        continue

      # NOTE: I think this can be cleaner where we're
      # not always looking ahead
      if token == 'li':
        # this is where things get gnarly
        # If we get a list, we want to lookahead by
        # incrementing the reader and pulling together
        # all the lines of the list until we're out
        list_out = ['<ul>', cls.html_tag_text(token, clean_text)]
        
        for next_token, next_text in cls.traverse_ahead(reader, 'li'):
          list_out.append(cls.html_tag_text(next_token, next_text))
            
        list_out.append('</ul>')
        html_out.append(''.join(list_out))
      elif token == 'p':
        # Same craziness as the list traversal
        p_out = ['<p>', clean_text]
        
        for _, next_text in cls.traverse_ahead(reader, 'p'):
            p_out.extend(['<br/>', next_text])
            
        p_out.append('</p>')
        html_out.append(''.join(p_out))
      else:
        # Header tag case, just append it and move on
        html_out.append(cls.html_tag_text(token, clean_text))
      
    return r"".join(html_out)

class Test():
  
  def test_parse_line_header(self):
    token, clean_text = MarkdownParser.parse_line('### This is a header')
    assert token == 'h3'
    assert clean_text == 'This is a header'
  
  def test_parse_line_list(self):
    token, clean_text = MarkdownParser.parse_line('* This is a list')
    assert token == 'li'
    assert clean_text == 'This is a list'
  
  
  def test_parse_line_paragraph(self):
    token, clean_text = MarkdownParser.parse_line('This is a paragraph')
    assert token == 'p'
    assert clean_text == 'This is a paragraph'
  
  def test_parse_line_empty(self):
    token, clean_text = MarkdownParser.parse_line('')
    assert token == None
    assert clean_text == ''
  
  
  def test_parse_header(self):
    html = MarkdownParser.to_html('# This is a header\n### This is a header\n\n')
    should_be = r'<h1>This is a header</h1><h3>This is a header</h3>'
    assert html == should_be
  
  def test_parse_list(self):
    html = MarkdownParser.to_html('* This is a list item\n* Another list item\n* one more')
    should_be = r'<ul><li>This is a list item</li><li>Another list item</li><li>one more</li></ul>'
    assert html == should_be
  
  def test_parse_paragraph(self):
    html = MarkdownParser.to_html('paragraph')
    should_be = r'<p>paragraph</p>'
    assert html == should_be
  
  def test_multiple_paragraphs(self):
    html = MarkdownParser.to_html('paragraph\n\npara2')
    should_be = r'<p>paragraph</p><p>para2</p>'
    assert html == should_be
  
  def test_line_break(self):
    html = MarkdownParser.to_html('break\nit\ndown\n\nnew para')
    should_be = r'<p>break<br/>it<br/>down</p><p>new para</p>'
    assert html == should_be

  def test_mixed_parse(self):
    html = MarkdownParser.to_html('# This is a header\n### This is a header\nThis is a paragraph\n* This is a list item\n* Another list item\nPara\nLinebreak para\nAnother line break para\n\nNew Para\n* new list')
    should_be = r'<h1>This is a header</h1><h3>This is a header</h3><p>This is a paragraph</p><ul><li>This is a list item</li><li>Another list item</li></ul><p>Para<br/>Linebreak para<br/>Another line break para</p><p>New Para</p><ul><li>new list</li></ul>'
    assert html == should_be
    
  def run(self):
    self.test_parse_line_header()
    self.test_parse_line_list()
    self.test_parse_line_paragraph()
    self.test_parse_line_empty()
    self.test_parse_header()
    self.test_parse_list()
    self.test_parse_paragraph()
    self.test_multiple_paragraphs()
    self.test_mixed_parse()
  
Test().run()