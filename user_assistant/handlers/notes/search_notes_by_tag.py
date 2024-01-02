from typing import Type
from functools import reduce
import operator

from user_assistant.notes.notes import Notes
from user_assistant.console.console import Console
from user_assistant.class_fields.tag import Tag
from user_assistant.handlers.input_value import input_value
from user_assistant.console.table_format.notes_table import note_titles, get_notes_row




def search_notes_by_tag(notes: Notes):
    list_tags = list((map(lambda el:  el.str_tags, notes.data.values())))
    
    prompts = lambda all_values: [el for list_tags in all_values for el in list_tags]
   
    tag = input_value('tag', Tag, prompts=set(prompts(list_tags)))
    result_notes = notes.search_by_tags(tag.value)
    Console.print_table(f"Notes found for tag: {tag}", note_titles, list(map(get_notes_row,result_notes)))

