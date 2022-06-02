import "./Results.css";
import { Link, useSearchParams } from 'react-router-dom';
import axios from 'axios'
import SearchEntries from "./SearchEntries";
import NotFound from "../NotFound/NotFound";
import { useEffect, useState } from "react";




const Results = (props) => {

  const [searchParams] = useSearchParams();
  const [companies, setCompanies] = useState('');
  const [query, setQuery] = useState(searchParams.get("q"));
  const [notDone,setNotDone] = useState(true);
  const [data,setData]=useState([]);





  useEffect(() => {
    localStorage.setItem("db", JSON.stringify(companies));
    notDone && getCompanies(query);

  }, [companies]);


  const getCompanies = (query) => {
    const url = 'http://127.0.0.1:5000/search'
    axios.get(url, { params: { q: query } })
      .then((response) => {
        setData(response.data);
        setNotDone(false);
      })
      .catch(error => console.error(`Errror : ${error}`))
  }

console.log(companies)

  return (
    <div>
      <h1>Hello Results</h1>
      {companies &&<SearchEntries  setCompany = {props.setCompany} data={data} />}
    </div>
  )


}

export default Results