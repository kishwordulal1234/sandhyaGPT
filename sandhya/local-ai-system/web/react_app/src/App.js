// web/react_app/src/App.js
import React, { useState } from 'react';
import Header from './components/Header';
import ChatWindow from './components/ChatWindow';
import Footer from './components/Footer';
import './styles/main.css';

function App() {
	const [messages, setMessages] = useState([]);
	
	const handleSendMessage = (message) => {
		// Add logic to send message to your AI model
		// Update state with new messages
	};
	
	return (
		<div className="App">
		<Header />
		<ChatWindow messages={messages} onSendMessage={handleSendMessage} />
		<Footer />
		</div>
	);
}

export default App;
