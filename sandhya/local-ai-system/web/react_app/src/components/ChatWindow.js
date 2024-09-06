// web/react_app/src/components/ChatWindow.js
import React, { useState } from 'react';

function ChatWindow({ messages, onSendMessage }) {
	const [input, setInput] = useState('');
	
	const handleSubmit = (e) => {
		e.preventDefault();
		onSendMessage(input);
		setInput('');
	};
	
	return (
		<main>
		<div className="chat-window">
		{messages.map((msg, index) => (
			<div key={index} className="message">{msg}</div>
		))}
		</div>
		<form onSubmit={handleSubmit}>
		<input
		type="text"
		value={input}
		onChange={(e) => setInput(e.target.value)}
		placeholder="Type a message..."
		/>
		<button type="submit">Send</button>
		</form>
		</main>
	);
}

export default ChatWindow;
