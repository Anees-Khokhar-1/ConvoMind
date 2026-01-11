async function sendMessage() {
    const input = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");

    const message = input.value.trim();
    if (!message) return;

    chatBox.innerHTML += `<div class="user">You: ${message}</div>`;
    input.value = "";

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message })
        });

        const data = await response.json();
        chatBox.innerHTML += `<div class="bot">Bot: ${data.reply}</div>`;
        chatBox.scrollTop = chatBox.scrollHeight;

    } catch (error) {
        chatBox.innerHTML += `<div class="error">❌ Server error</div>`;
    }
}
