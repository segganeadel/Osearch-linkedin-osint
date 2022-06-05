import "./Company.css";
import axios from 'axios';
import { useLocation } from 'react-router-dom';
import { useEffect, useState } from "react";

const Company = (props) => {



  const [company, setCompany] = useState('');
  const location = useLocation();


  useEffect(() => {
    getCompany();

  }, []);

  const getCompany = () => {
    
    const url = 'http://127.0.0.1:5000/company'
    axios.get(url, { params: { 
      q: location.pathname}
       })
      .then((response) => {
        setCompany(response.data);
      })
      .catch(error => console.error(`Errror : ${error}`))
  }

  console.log(props)

  return (
  <div>
    {company && <h3>{company.company.companyname}</h3>}
  </div>
  )
}

export default Company