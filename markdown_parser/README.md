# Markdown to HTML Parser

## Problem Statement
Write a simplified Markdown to HTML converter using the language of your choice.

Example input Markdown string: "# This is a header\nThis is a paragraph\n* This is a list item\n* Another list item"

Example output HTML string: "<h1>This is a header</h1><p>This is a paragraph</p><ul><li>This is a list item</li><li>Another list item</li></ul>"

You only need to care about the Markdown blocks provided in the 9 example input/output pairs below and don’t need to handle inline or nested blocks.

Input Markdown          | Output HTML
---------------------------------------------------------
# This is a header      | <h1>This is a header</h1>
---------------------------------------------------------
## Smaller header       | <h2>Smaller header</h2>
---------------------------------------------------------
This is a paragraph     | <p>This is a paragraph</p>
                        |
---------------------------------------------------------
* This is a list item   | <ul>
* Another list item     |   <li>This is a list item</li>
* Another list item     |   <li>Another list item</li>
* Another list item     |   <li>Another list item</li>
                        |   <li>Another list item</li>
                        | </ul>
---------------------------------------------------------
# This is a header      | <h1>This is a header</h1>
This is a paragraph     | <p>This is a paragraph</p>
* This is a list item   | <ul>
* Another list item     |   <li>This is a list item</li> 
                        |   <li>Another list item</li>
                        | </ul>  
---------------------------------------------------------
This is a paragraph     | <p>This is a paragraph<br/>
with a line break       | with a line break</p>
---------------------------------------------------------
This is a paragraph     | <p>This is a paragraph</p>
                        | <p>Another paragraph</p>
Another paragraph       |
---------------------------------------------------------
Not # a header          | <p>Not # a header</p>
---------------------------------------------------------
This is a paragraph     | <p>This is a paragraph</p>
                        | <p>Another paragraph</p>
                        |
Another paragraph       |
--------------------------------------------------------- 

## Notes
This was scheduled for 30 mins and did not complete in the 30, took over an hour to write this out.

This could still use some better abstraction. If we were to add some more complicatd Markdown, we'd want to do this in another way. I took some shortcuts cause we got a limited known set.