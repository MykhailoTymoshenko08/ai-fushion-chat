import { useState } from 'react';

export default function Home() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');
  const [token, setToken] = useState('');

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setMessage('⌛ Входимо...');
    setToken('');
    
    try {
      const response = await fetch('http://127.0.0.1:8000/auth/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, password }),
      });
      
      console.log('Статус відповіді:', response.status);
      
      if (response.ok) {
        const data = await response.json();
        console.log('Отримані дані:', data);
        
        setToken(data.access_token);
        setMessage(`✅ Успішний вхід!`);
      } else {
        const errorText = await response.text();
        console.log('Помилка відповіді:', errorText);
        
        try {
          const errorData = JSON.parse(errorText);
          setMessage(`❌ Помилка: ${errorData.detail || 'Невідома помилка'}`);
        } catch {
          setMessage(`❌ Помилка: ${response.status} - ${errorText}`);
        }
      }
    } catch (error) {
      console.error('Помилка підключення:', error);
      setMessage('❌ Помилка підключення до сервера');
    }
  };

  return (
    <div style={{ 
      padding: '50px', 
      fontFamily: 'Arial, sans-serif',
      maxWidth: '500px',
      margin: '0 auto',
      backgroundColor: '#f5f5f5',
      minHeight: '100vh'
    }}>
      <h1 style={{ color: '#333', textAlign: 'center' }}>🤖 AI Fusion Chat</h1>
      <p style={{ textAlign: 'center', color: '#666' }}>Чат-платформа з інтеграцією кількох AI моделей</p>
      
      <div style={{
        backgroundColor: 'white',
        padding: '30px',
        borderRadius: '10px',
        boxShadow: '0 2px 10px rgba(0,0,0,0.1)',
        marginTop: '20px'
      }}>
        <h3 style={{ marginBottom: '20px' }}>Вхід в систему</h3>
        
        <form onSubmit={handleLogin}>
          <div style={{ marginBottom: '15px' }}>
            <input
              type="email"
              placeholder="Email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              style={{ 
                width: '100%', 
                padding: '12px', 
                fontSize: '16px',
                border: '1px solid #ddd',
                borderRadius: '5px',
                boxSizing: 'border-box'
              }}
              required
            />
          </div>
          
          <div style={{ marginBottom: '20px' }}>
            <input
              type="password"
              placeholder="Password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              style={{ 
                width: '100%', 
                padding: '12px', 
                fontSize: '16px',
                border: '1px solid #ddd',
                borderRadius: '5px',
                boxSizing: 'border-box'
              }}
              required
            />
          </div>
          
          <button 
            type="submit" 
            style={{ 
              width: '100%', 
              padding: '12px', 
              fontSize: '16px', 
              backgroundColor: '#007acc',
              color: 'white',
              border: 'none',
              borderRadius: '5px',
              cursor: 'pointer'
            }}
          >
            Увійти
          </button>
        </form>
        
        {message && (
          <div style={{ 
            marginTop: '20px', 
            padding: '15px', 
            backgroundColor: message.includes('✅') ? '#d4edda' : '#f8d7da',
            border: '1px solid',
            borderColor: message.includes('✅') ? '#c3e6cb' : '#f5c6cb',
            borderRadius: '5px',
            color: message.includes('✅') ? '#155724' : '#721c24'
          }}>
            <strong>{message}</strong>
            {token && (
              <div style={{ marginTop: '10px', fontSize: '14px' }}>
                <p>🔑 Токен: {token.substring(0, 50)}...</p>
                <button 
                  onClick={() => {
                    navigator.clipboard.writeText(token);
                    alert('Токен скопійовано!');
                  }}
                  style={{ 
                    padding: '5px 10px', 
                    fontSize: '12px',
                    marginTop: '5px'
                  }}
                >
                  📋 Копіювати токен
                </button>
              </div>
            )}
          </div>
        )}
        
        <div style={{ marginTop: '30px', fontSize: '14px', color: '#666' }}>
          <p><strong>Тестові дані:</strong></p>
          <p>📧 Email: test@example.com</p>
          <p>🔑 Password: password123</p>
        </div>

        {token && (
          <div style={{ marginTop: '20px', textAlign: 'center' }}>
            <a 
              href="/chat" 
              style={{ 
                display: 'inline-block',
                padding: '10px 20px',
                backgroundColor: '#28a745',
                color: 'white',
                textDecoration: 'none',
                borderRadius: '5px',
                fontSize: '16px'
              }}
            >
              🚀 Перейти до чату
            </a>
          </div>
        )}
      </div>
    </div>
  );
}