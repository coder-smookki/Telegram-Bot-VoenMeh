import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.jsx'
import './App.scss'
createRoot(document.getElementById('app')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
