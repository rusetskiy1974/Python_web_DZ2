from user_assistant.notes.note_record import NoteRecord


note_titles = ["🤠 Author", "📝 Text", "🖇 Tags", "🎱 ID", "📅 Created at"]


def get_notes_row(record: NoteRecord):
    return [
        record.author.value,
        record.text.value,
        ', '.join(record.str_tags),
        record.id.value,
        str(record.created_at),
    ]