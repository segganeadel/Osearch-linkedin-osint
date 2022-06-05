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
  const [active, setActive] = useState(searchParams.get("active"));

  useEffect(() => {
   

  }, []);

  const getCompanies = async (query, active) => {
    const url = 'http://127.0.0.1:5000/search'
    try {
      const resp = await axios.get(url, {
        params: {
          a: active,
          q: query
        }
      })
      setCompanies(resp.data);

    }
    catch (err) {
      // Handle Error Here
      console.error(err);
    }
  };
  getCompanies(query, active);
  if (companies.results.length === 0) { return (<NotFound />) }
  else {
    return (
      <div>

        <h1>Hello Results</h1>
        {companies && <SearchEntries data={companies} active={active} />
        }
      </div>
    )
  }
}

export default Results