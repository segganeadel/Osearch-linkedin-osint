import "./Results.scss";
import { Link, useSearchParams } from 'react-router-dom';
import axios from 'axios'
import SearchEntries from "../../components/searchentries/SearchEntries";
import NotFound from "../NotFound/NotFound";
import { useEffect, useState } from "react";
import Loader from "../../components/loader/Loader";
import Erreur from "../../components/erreur/Erreur";



const Results = (props) => {

  const [searchParams] = useSearchParams();
  const [companies, setCompanies] = useState('');
  const [wait, setWait] = useState(true)
  const [erreur, setErreur] = useState('');
  const [query, setQuery] = useState(searchParams.get("q"));

  useEffect(() => {
    getCompanies(query);
  }, []);

  const getCompanies = async (query) => {
    const url = 'http://127.0.0.1:5000/search'


    try {
      const resp = await axios.get(url, {
        params: {
          q: query
        }
      })
      setCompanies(resp.data);
      setWait(false)
    }
    catch (err) {
      // Handle Error Here
      console.error(err);
      setErreur(err)
      setWait(false)
    }
  };

  if (wait) {
    return(
      <div >
      <Loader />
    </div>
    )}
  else {
    return (
      <div>
        <div className="result_block">
          {
            ((erreur) && (<Erreur code={erreur.code} />)) || (<SearchEntries data={companies} />)
          }
        </div>
      </div>
    )
  }

}


export default Results