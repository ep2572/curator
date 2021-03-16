# curator
A private chatroom service featuring drawing and editing capabilities for collaboration, instruction, and review.

To be written in Python.

A roadmap can be found in the [design document](curatorDesignDoc.txt)

## Initial Requirements
- User must be able to set up a private chatroom with a unique roomkey without the need for accounts.
  - User data for a room will be linked to the user's IP address
  - Data will be cleared once last user leaves the chatroom
- Chat Functionality:
  - `Whisper`: w/username or whisper/username (Private message one other user in the chatroome)
  - `Notify`: @username or at/username or n/username or notify/username
  - `Mute`: m/username or mute/username (Host feature)
  - `Kick`: k/username or lick/username (Host feature)
- Main body of the page will diplay the sample file(for now just .jpeg, .png, .gif, .bmp) overlayed with an editing layer
  - Anyone will submit to thePermission to submit is provided by the host
  - All in attendance will be able to draw or type on the editing layer given host permission.
- Users will be able to save and print modified samples as .jpeg files.
  - Links to the system's `Save As` and `Print` dialogue boxes using an API

## Design
(to be filled)
