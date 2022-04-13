text_changed=False
# def changed(event=None):
#     if text_editor.edit_modified():
#         text_changed=True
#         words=len(text_editor.get(1.0,'end-1c').split())
#         characters=len(text_editor.get(1.0,'end-1c'))
#         status_bar.config(text=f'Words : {words} Characters : {characters}')
#     text_editor.edit_modified(False)

# text_editor.bind('<<Modified>>',changed)