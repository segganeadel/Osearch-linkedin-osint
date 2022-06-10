import "./Company.scss";
import axios from 'axios';
import { useLocation } from 'react-router-dom';
import { useEffect, useState } from "react";
import Data from "../../components/Data/Data";
import Loader from "../../components/loader/Loader";
import Erreur from "../../components/erreur/Erreur";
import Jobs from "../../components/jobs/Jobs";

const Company = (props) => {



  const [company, setCompany] = useState('');
  const [wait, setWait] = useState(true);
  const [erreur, setErreur] = useState('');


  const location = useLocation();


  useEffect(() => {
    getCompany();
  }, []);

  const getCompany = async () => {

    const url = 'http://127.0.0.1:5000/company'

    try {
      const resp = await axios.get(url, {
        params: {
          q: location.pathname
        }
      })
      setCompany(resp.data);
      setWait(false)
    }
    catch (err) {
      // Handle Error Here
      console.error(err);
      setErreur(err)
      setWait(false)

    }
  }

  if (wait) {
    return (
      <div className="load">
        <Loader />
      </div>
    )
  }
  else {
    return (
      <div className="flexbox">
        <div className="title">
          <h2>Resultats de la recherche :</h2>
        </div>
        <div>
          {
            ((erreur) && (<Erreur code={erreur.code} />)) || (<Data data={company} />)
          }
        </div>
        <div >
          <button>
            Pus d'informations
          </button>
        </div>     
      </div>
    )
  }
}

export default Company