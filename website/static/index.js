function deleteNote(noteId){
    // sending  a request with fetch
    fetch ("/delete-note", {
        method: "POST",
        body: JSON.stringify({noteId: noteId}),
    }).then((_res) => {
        // reloading the window
        window.location.href = "/";
    });
}