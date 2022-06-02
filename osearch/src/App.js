import './App.css';
import Home from './components/Home/Home';
import Results from './components/Results/Results';
import Company from './components/Company/Company'
import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";
import { useState, } from "react";


function App() {
  const [company, setCompany] = useState('');

  return (
    <div className="container">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/results" element={<Results setCompany={setCompany}/>} />
          <Route path="/:company" element={<Company data={company}/>} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
