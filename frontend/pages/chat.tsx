// import { useState, useEffect } from 'react';

// interface Message {
//   id: number;
//   content: string;
//   role: 'user' | 'assistant';
//   created_at: string;
// }

// export default function ChatPage() {
//   const [message, setMessage] = useState('');
//   const [chatId, setChatId] = useState<number | null>(null);
//   const [messages, setMessages] = useState<Message[]>([]);
//   const [loading, setLoading] = useState(false);
//   const [selectedModel, setSelectedModel] = useState('all');

//   // Створюємо новий чат при завантаженні
//   useEffect(() => {
//     createChat();
//   }, []);

//   const createChat = async () => {
//     try {
//       const response = await fetch('http://127.0.0.1:8000/chat/chats?title=Мій+AI+чат', {
//         method: 'POST'
//       });
//       const chat = await response.json();
//       setChatId(chat.id);
//       console.log('Чат створений:', chat.id);
//     } catch (error) {
//       console.error('Помилка створення чату:', error);
//     }
//   };

//   const sendMessage = async (e: React.FormEvent) => {
//     e.preventDefault();
//     if (!message.trim() || !chatId) return;

//     setLoading(true);
//     try {
//       let url: string;
      
//       if (selectedModel === 'all') {
//         // Відправляємо всім моделям
//         url = `http://127.0.0.1:8000/chat/chats/${chatId}/message?message=${encodeURIComponent(message)}`;
//       } else {
//         // Відправляємо конкретній моделі
//         url = `http://127.0.0.1:8000/chat/chats/${chatId}/message/${selectedModel}?message=${encodeURIComponent(message)}`;
//       }

//       console.log('Відправляємо запит до:', url);
//       const response = await fetch(url, { method: 'POST' });
      
//       if (!response.ok) {
//         throw new Error(`HTTP error! status: ${response.status}`);
//       }
      
//       const result = await response.json();
//       console.log('Отримана відповідь:', result);

//       // Оновлюємо список повідомлень
//       if (selectedModel === 'all') {
//         // Додаємо повідомлення користувача
//         const userMessage: Message = {
//           id: Date.now(),
//           content: message,
//           role: 'user',
//           created_at: new Date().toISOString()
//         };
        
//         setMessages(prev => [...prev, userMessage]);
        
//         // Додаємо всі AI відповіді
//         if (result.ai_responses) {
//           Object.entries(result.ai_responses).forEach(([model, response]) => {
//             const aiMessage: Message = {
//               id: Date.now() + Math.random(),
//               content: `[${model.toUpperCase()}] ${response}`,
//               role: 'assistant',
//               created_at: new Date().toISOString()
//             };
//             setMessages(prev => [...prev, aiMessage]);
//           });
//         }
//       } else {
//         // Для однієї моделі - використовуємо правильну структуру
//         const userMessage: Message = {
//           id: Date.now(),
//           content: `[${selectedModel.toUpperCase()}] ${message}`,
//           role: 'user',
//           created_at: new Date().toISOString()
//         };

//         // Використовуємо ai_response замість ai_response.content
//         const aiResponse = result.ai_response || 'Немає відповіді';
//         const aiMessage: Message = {
//           id: Date.now() + 1,
//           content: aiResponse,
//           role: 'assistant',
//           created_at: new Date().toISOString()
//         };

//         setMessages(prev => [...prev, userMessage, aiMessage]);
//       }
      
//       setMessage('');
//     } catch (error) {
//       console.error('Помилка відправки:', error);
//       alert(`Помилка відправки повідомлення: ${error}`);
//     } finally {
//       setLoading(false);
//     }
//   };

//   const getMessageStyle = (msg: Message) => {
//     const baseStyle = {
//       display: 'inline-block',
//       padding: '10px 15px',
//       borderRadius: '15px',
//       maxWidth: '70%',
//       marginBottom: '10px',
//       wordWrap: 'break-word' as const
//     };

//     if (msg.role === 'user') {
//       return {
//         ...baseStyle,
//         backgroundColor: '#007acc',
//         color: 'white',
//         marginLeft: 'auto',
//         textAlign: 'right' as const
//       };
//     } else {
//       // Визначаємо колір для кожної моделі
//       let backgroundColor = '#f1f1f1';
//       let borderColor = '#ddd';
      
//       if (msg.content.includes('[OPENAI]')) {
//         backgroundColor = '#e3f2fd';
//         borderColor = '#2196f3';
//       } else if (msg.content.includes('[CLAUDE]')) {
//         backgroundColor = '#f3e5f5';
//         borderColor = '#9c27b0';
//       } else if (msg.content.includes('[GEMINI]')) {
//         backgroundColor = '#e8f5e8';
//         borderColor = '#4caf50';
//       } else if (msg.content.includes('[MISTRAL]')) {
//         backgroundColor = '#fff3e0';
//         borderColor = '#ff9800';
//       }

//       return {
//         ...baseStyle,
//         backgroundColor,
//         color: 'black',
//         border: `1px solid ${borderColor}`,
//         textAlign: 'left' as const
//       };
//     }
//   };

//   return (
//     <div style={{ padding: '20px', maxWidth: '800px', margin: '0 auto', fontFamily: 'Arial, sans-serif' }}>
//       <h1>🤖 AI Fusion Chat</h1>
//       <p>Спілкуйтесь з 2 різними AI моделями одночасно!</p>
      
//       {/* Вибір моделі */}
//       <div style={{ marginBottom: '20px', padding: '15px', backgroundColor: '#f8f9fa', borderRadius: '10px' }}>
//         <label style={{ marginRight: '10px', fontWeight: 'bold' }}>Оберіть модель:</label>
//         <select 
//   value={selectedModel} 
//   onChange={(e) => setSelectedModel(e.target.value)}
//   style={{ padding: '8px', borderRadius: '5px', border: '1px solid #ddd' }}
// >
//   <option value="all">🎭 Обидві моделі</option>
//   <option value="groq">🚀 Groq</option>
//   <option value="huggingface">🤗 Hugging Face</option>
// </select>
        
//         <div style={{ marginTop: '10px', fontSize: '14px', color: '#666' }}>
//           {selectedModel === 'all' 
//             ? '💡 Повідомлення буде відправлено всім 4 моделям одночасно'
//             : `💡 Повідомлення буде відправлено тільки ${selectedModel}`}
//         </div>
//       </div>

//       {/* Вікно чату */}
//       <div style={{ 
//         border: '1px solid #ccc', 
//         height: '400px', 
//         overflowY: 'auto', 
//         padding: '20px',
//         marginBottom: '20px',
//         backgroundColor: '#fafafa',
//         borderRadius: '10px'
//       }}>
//         {messages.length === 0 ? (
//           <div style={{ textAlign: 'center', color: '#666', marginTop: '50px' }}>
//             <p>👋 Почніть розмову!</p>
//             <p>Оберіть модель та напишіть повідомлення</p>
//           </div>
//         ) : (
//           messages.map((msg, index) => (
//             <div key={index} style={{ 
//               marginBottom: '10px',
//               display: 'flex',
//               justifyContent: msg.role === 'user' ? 'flex-end' : 'flex-start'
//             }}>
//               <div style={getMessageStyle(msg)}>
//                 {msg.content}
//               </div>
//             </div>
//           ))
//         )}
//         {loading && (
//           <div style={{ textAlign: 'center', color: '#666', fontStyle: 'italic' }}>
//             ⌛ AI думає...
//           </div>
//         )}
//       </div>

//       {/* Форма відправки */}
//       <form onSubmit={sendMessage} style={{ display: 'flex', gap: '10px', alignItems: 'center' }}>
//         <input
//           type="text"
//           value={message}
//           onChange={(e) => setMessage(e.target.value)}
//           placeholder="Напишіть повідомлення..."
//           style={{ 
//             flex: 1, 
//             padding: '12px', 
//             fontSize: '16px',
//             border: '1px solid #ddd',
//             borderRadius: '5px'
//           }}
//           disabled={loading}
//         />
//         <button 
//           type="submit" 
//           disabled={loading || !message.trim()}
//           style={{ 
//             padding: '12px 24px', 
//             fontSize: '16px',
//             backgroundColor: loading ? '#ccc' : '#007acc',
//             color: 'white',
//             border: 'none',
//             borderRadius: '5px',
//             cursor: loading ? 'not-allowed' : 'pointer'
//           }}
//         >
//           {loading ? '⌛' : '📤'} Надіслати
//         </button>
//       </form>

//       {/* Легенда моделей */}
//       <div style={{ marginTop: '20px', fontSize: '14px', color: '#666' }}>
//         <p><strong>🎨 Кольори моделей:</strong></p>
//         <div style={{ display: 'flex', gap: '15px', flexWrap: 'wrap' }}>
//           <span style={{ backgroundColor: '#e3f2fd', padding: '2px 8px', borderRadius: '3px' }}>🚀 Groq</span>
//           <span style={{ backgroundColor: '#f3e5f5', padding: '2px 8px', borderRadius: '3px' }}>🤗 Hugging Face</span>
//         </div>
//       </div>
//     </div>
//   );
// }






import { useState, useEffect } from 'react';

interface Message {
  id: number;
  content: string;
  role: 'user' | 'assistant';
  created_at: string;
}

export default function ChatPage() {
  const [message, setMessage] = useState('');
  const [chatId, setChatId] = useState<number | null>(null);
  const [messages, setMessages] = useState<Message[]>([]);
  const [loading, setLoading] = useState(false);
  const [selectedModel, setSelectedModel] = useState('all');

  // Створюємо новий чат при завантаженні
  useEffect(() => {
    createChat();
  }, []);

  const createChat = async () => {
    try {
      const response = await fetch('http://127.0.0.1:8000/chat/chats?title=Мій+AI+чат', {
        method: 'POST'
      });
      const chat = await response.json();
      setChatId(chat.id);
      console.log('Чат створений:', chat.id);
    } catch (error) {
      console.error('Помилка створення чату:', error);
    }
  };

  const sendMessage = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!message.trim() || !chatId || loading) return;

    setLoading(true);
    const userMessage = message;
    setMessage(''); // Очищаємо поле одразу
    
    try {
      // Додаємо повідомлення користувача
      const userMsg: Message = {
        id: Date.now(),
        content: userMessage,
        role: 'user',
        created_at: new Date().toISOString()
      };
      setMessages(prev => [...prev, userMsg]);

      let url: string;
      
      if (selectedModel === 'all') {
        url = `http://127.0.0.1:8000/chat/chats/${chatId}/message?message=${encodeURIComponent(userMessage)}`;
      } else {
        url = `http://127.0.0.1:8000/chat/chats/${chatId}/message/${selectedModel}?message=${encodeURIComponent(userMessage)}`;
      }

      console.log('Відправляємо запит до:', url);
      
      const response = await fetch(url, { 
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        }
      });
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      
      const result = await response.json();
      console.log('Отримана відповідь:', result);

      // Обробляємо відповіді
      if (selectedModel === 'all') {
        // Додаємо всі AI відповіді
        if (result.ai_responses) {
          Object.entries(result.ai_responses).forEach(([model, response]) => {
            const aiMsg: Message = {
              id: Date.now() + Math.random(),
              content: `${response}`,
              role: 'assistant',
              created_at: new Date().toISOString()
            };
            setMessages(prev => [...prev, aiMsg]);
          });
        }
      } else {
        // Для однієї моделі
        const aiMsg: Message = {
          id: Date.now() + 1,
          content: result.ai_response || 'Немає відповіді',
          role: 'assistant',
          created_at: new Date().toISOString()
        };
        setMessages(prev => [...prev, aiMsg]);
      }
      
    } catch (error) {
      console.error('Помилка відправки:', error);
      const errorMsg: Message = {
        id: Date.now() + 1,
        content: '❌ Помилка відправки повідомлення',
        role: 'assistant',
        created_at: new Date().toISOString()
      };
      setMessages(prev => [...prev, errorMsg]);
    } finally {
      setLoading(false);
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage(e);
    }
  };

  const getMessageStyle = (msg: Message) => {
    const baseStyle = {
      display: 'inline-block',
      padding: '10px 15px',
      borderRadius: '15px',
      maxWidth: '70%',
      marginBottom: '10px',
      wordWrap: 'break-word' as const
    };

    if (msg.role === 'user') {
      return {
        ...baseStyle,
        backgroundColor: '#007acc',
        color: 'white',
        marginLeft: 'auto',
        textAlign: 'right' as const
      };
    } else {
      let backgroundColor = '#f1f1f1';
      
      if (msg.content.includes('🚀 Groq')) {
        backgroundColor = '#e3f2fd';
      } else if (msg.content.includes('🤗 Hugging Face')) {
        backgroundColor = '#f3e5f5';
      }

      return {
        ...baseStyle,
        backgroundColor,
        color: 'black',
        border: '1px solid #ddd',
        textAlign: 'left' as const
      };
    }
  };

  return (
    <div style={{ padding: '20px', maxWidth: '800px', margin: '0 auto', fontFamily: 'Arial, sans-serif' }}>
      <h1>🤖 AI Fusion Chat</h1>
      <p>Спілкуйтесь з AI моделями</p>
      
      {/* Вибір моделі */}
      <div style={{ marginBottom: '20px', padding: '15px', backgroundColor: '#f8f9fa', borderRadius: '10px' }}>
        <label style={{ marginRight: '10px', fontWeight: 'bold' }}>Оберіть модель:</label>
        <select 
          value={selectedModel} 
          onChange={(e) => setSelectedModel(e.target.value)}
          style={{ padding: '8px', borderRadius: '5px', border: '1px solid #ddd' }}
        >
          <option value="all">🎭 Обидві моделі</option>
          <option value="groq">🚀 Groq</option>
          <option value="huggingface">🤗 Hugging Face</option>
        </select>
      </div>

      {/* Вікно чату */}
      <div style={{ 
        border: '1px solid #ccc', 
        height: '400px', 
        overflowY: 'auto', 
        padding: '20px',
        marginBottom: '20px',
        backgroundColor: '#fafafa',
        borderRadius: '10px'
      }}>
        {messages.length === 0 ? (
          <div style={{ textAlign: 'center', color: '#666', marginTop: '50px' }}>
            <p>👋 Почніть розмову!</p>
            <p>Оберіть модель та напишіть повідомлення</p>
          </div>
        ) : (
          messages.map((msg, index) => (
            <div key={index} style={{ 
              marginBottom: '10px',
              display: 'flex',
              justifyContent: msg.role === 'user' ? 'flex-end' : 'flex-start'
            }}>
              <div style={getMessageStyle(msg)}>
                {msg.content}
              </div>
            </div>
          ))
        )}
        {loading && (
          <div style={{ textAlign: 'center', color: '#666', fontStyle: 'italic' }}>
            ⌛ AI думає...
          </div>
        )}
      </div>

      {/* Форма відправки */}
      <form onSubmit={sendMessage} style={{ display: 'flex', gap: '10px', alignItems: 'center' }}>
        <input
          type="text"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          onKeyPress={handleKeyPress}
          placeholder="Напишіть повідомлення..."
          style={{ 
            flex: 1, 
            padding: '12px', 
            fontSize: '16px',
            border: '1px solid #ddd',
            borderRadius: '5px'
          }}
          disabled={loading}
        />
        <button 
          type="submit" 
          disabled={loading || !message.trim()}
          style={{ 
            padding: '12px 24px', 
            fontSize: '16px',
            backgroundColor: loading ? '#ccc' : '#007acc',
            color: 'white',
            border: 'none',
            borderRadius: '5px',
            cursor: loading ? 'not-allowed' : 'pointer'
          }}
        >
          {loading ? '⌛' : '📤'} Надіслати
        </button>
      </form>
    </div>
  );
}