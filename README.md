# curator
A private chatroom service featuring drawing and editing capabilities for collaboration, instruction, and review.

To be written in Python.

A roadmap can be found [here](roadmap.txt)

## Initial Requirements
- The application homepage will contain two main sections:  
    1. Join An Existing Room  
      - Text boxes:  
        <ul>
            <li>[Enter Username] -- which will provide an alias linked to the user's IP address for display in the chatroom.</li>
            <li>[Enter Roomkey] -- which will allow access to a room, if that room exists and is not at capacity.</li>
        </ul>
    2.  Create A New Room  
      - Text boxes:    
        <ul>
            <li>Title</li>
            <li>Capacity (max 32(?))</li>
            <li>Note -- a preemtive notification provided before entering a room. e.g. "Warning: Avenger's spoilers ahead!!!"</li>
        </ul>
       - Buttons:  
        - `Create Room`   
  - The homepage will also contain links:  
    <ul>
        <li>`How To Use` -- this page provides a description of the app.</li>
        <li>`About` -- this about page contains shorts bios of all parties involved.</li>
    </ul>
- User must be able to set up a chatroom with a unique roomkey without the need for accounts.
  - User data for a room will be linked to the user's IP address
  - Data will be cleared once last user leaves the chatroom
- Chat Functionality:
  - Hosts have all Moderator privileges
  - Whisper: `w/username` or `whisper/username` (Private message one other user in the chatroome)
  - Notify: `@username` or `at/username` or n/username or notify/username (provides a sound effect and highlights the message for target user)
  - Mute: `m/username` or `mute/username` (Moderator feature)
  - Kick: `k/username` or `kick/username` (Moderator feature)
  - Make Moderator: `mod/username` (Host feature)
  - Remove Moderator: `rmod/username` (Host feature)
  - Change Host: `host/username` (Host feature: current host loses host privileges, but remains a Moderator)
- Main body of the page will diplay the sample file(for now just .jpeg, .png, .gif, .bmp) overlayed with an editing layer
  - Anyone will submit to thePermission to submit is provided by the host
  - All in attendance will be able to draw or type on the editing layer given host permission.
- Users will be able to save and print modified samples as .jpeg files.
  - Opens the system's `Save As` and `Print` dialogue boxes using an API

## Setup
1. Ensure that make and pip are properly installed on your system.
2. Enter `make dev_env` to create the build environment.
3. Use `make prod` to compile the application.

## Design
(to be filled)
