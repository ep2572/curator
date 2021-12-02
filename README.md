# curator
A private chatroom service featuring drawing and editing capabilities for collaboration, instruction, and review.

Written primarily in Python, HTML, and javascript

A roadmap can be found [here](roadmap.txt)  
A detailed wireframe can be found [here](sitemap.png)

## Current Implementation
- Basic room structure built
- Room key uniqueness enforcement
- Database models built
- app initialization: runnable without database access

## In Development
- data commits
- integration of database into app routes

## To Be Developed
- File Overlay
    - Max file size: 16 MB
    - 1 file per room, initially
- Link drawing overlay to rooms
- Implement chat commands
- Implement information window overlay
- Implement Save/Download feature

## Setup
1. Ensure that make and pip are properly installed on your system.
2. Enter `make dev_env` to create the build environment.
4. Use `make prod` to perform tests and push changes to github.

## Testing
- Use `make tests` to perform tests
- Use `./local.sh` to run the server on localhost:8000

## Documentation
- Use `make docs` to generate HTML documentation for .py source files

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
        - Buttons:  <br>
            <ul>
                <li>`Create Room`</li>
            </ul>
        - When a new room is created a 12 character password is generated and displayed just below the room name in the upper left, above the chat. The password is required for entry into the room.
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
  - Moderators cannot kick moderator or hosts
  - Whisper: `/w username` or `/whisper username` (Private message one other user in the chatroome)
  - Notify: `@username` or `/at username` or n/username or notify/username (provides a sound effect and highlights the message for target user)
  - Mute: `/m username` or `/mute username` (Moderator feature)
  - Kick: `/k username` or `/kick username` (Moderator feature)
  - Unkick: `/uk username` or `/unkick username` (Moderator feature)
  - Make Moderator: `/mod username` (Host feature)
  - Remove Moderator: `/rmod username` (Host feature)
  - Change Host: `/host username` (Host feature: current host loses host privileges, but remains a Moderator)
- Main body of the page will diplay the sample file(for now just .jpeg, .png, .gif, .bmp) overlayed with an editing layer
  - Only one file per chat (for now)
  - Only the host and moderators can upload files
  - All in attendance will be able to draw or type on the editing layer given host permission.
- Users will be able to save and print modified samples as .jpeg files.
  - Opens the system's `Save As` and `Print` dialogue boxes using an API
