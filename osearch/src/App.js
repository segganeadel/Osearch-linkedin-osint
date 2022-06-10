import './App.css';
import Home from './pages/Home/Home';
import Results from './pages/Results/Results';
import Company from './pages/Company/Company'
import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";
import { useState, } from "react";


function App() {
  return (
    <div className="container">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/results" element={<Results />} />
          <Route path="/:company" element={<Company />} >
            <Route />
          </Route>

        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
