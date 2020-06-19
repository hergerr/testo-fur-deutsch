import './App.css';
import React from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import { HomePage } from './pages/home-page/home-page.component';
import { ChooseSetPage } from './pages/choose-set-page/choose-set-page.component';
import { WordQuizPage } from './pages/word-quiz-page/word-quiz-page.component';

function App() {
  return (
    <div className="App">
    <p className="App-logo">LG</p>
      <Router>
        <div>
          <nav className="App-nav">
            <ul>
              <li>
                <Link to="/">Home</Link>
              </li>
              <li>
                <Link to="/choose">Choose</Link>
              </li>
              <li>
                <Link to="/word">Word</Link>
              </li>
            </ul>
          </nav>

          {/* A <Switch> looks through its children <Route>s and
            renders the first one that matches the current URL. */}
          <Switch>
            <Route path="/word">
              <WordQuizPage/>
            </Route>
            <Route path="/choose">
              <ChooseSetPage />            
            </Route>
            <Route path="/">
                <HomePage />
            </Route>
          </Switch>
        </div>
      </Router>
    </div>
  );
}

export default App;
