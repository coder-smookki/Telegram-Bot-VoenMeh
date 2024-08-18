import { useState } from 'react'
import { Route, BrowserRouter, HashRouter, Routes, Navigate } from "react-router-dom";


import Header from './UI/Header/header';
import Container from './components/Container/Container';

import Main from './components/Main/Main';
import Registration from './components/Registration/Registration';
import Birthday from './components/Registration/Birthday';
import Gender from './components/Registration/Gender';
import Interesting from './components/Registration/Interesting';

function App() {
  const [loggedIn, setLoggedIn] = useState(false)

  return (
    <>
      <HashRouter>
        <Header></Header>
        <Container>
          <Routes>
            <Route
              path='/'
              element={loggedIn ? <Main/> : <Navigate to='/register' replace />}>
              </Route>
            <Route
              path='/register'>
                <Route path='/register'
                element={loggedIn ? <Navigate to='/' replace/> : <Registration/>}
                />
                  <Route
                    path='/register/birthday'
                    element={<Birthday/>}
                  />
                  <Route
                    path='/register/gender'
                    element={<Gender/>}
                  />
                  <Route
                    path='/register/interesting'
                    element={<Interesting/>}
                  />
                  <Route
                    path='*'
                    element={loggedIn ? <Navigate to='/' replace/> : <Navigate to='/register' replace/>}
                  />
              </Route>
            <Route
              path="*"
              element={
              <Navigate to='/' replace />
              } />
          </Routes>
        </Container>
      </HashRouter>
    </>
  )
}

export default App
