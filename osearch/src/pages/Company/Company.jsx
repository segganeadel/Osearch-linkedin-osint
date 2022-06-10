import "./Company.css";
import axios from 'axios';
import { useLocation } from 'react-router-dom';
import { useEffect, useState } from "react";
import Data from "../../components/Data/Data";
import Loader from "../../components/loader/Loader";
import Erreur from "../../components/erreur/Erreur";

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



  const MoreInfo = () => {
    const url = 'http://127.0.0.1:5000/linkedin'
    var myName = prompt("Name Here:","")
    var myAge = prompt("Age Here:","")
    alert(myName +", you are "+ myAge +" years old!")
    // try {
    //   const resp = await axios.get(url, {
    //     params: {
    //       q: location.pathname
    //     }
    //   })
    //   setCompany(resp.data);
    //   setWait(false)
    // }
    // catch (err) {
    //   // Handle Error Here
    //   console.error(err);
    //   setErreur(err)
    //   setWait(false)

    // }
  }

  return (
    <div>
      <div>
        {
          (wait) && (<Loader />) || ((erreur) && (<Erreur code={erreur.code} />)) || (<Data data={company} />)
        }
      </div>
      <div className="button">
        <button onClick={MoreInfo}>
          Pus d'informations
        </button>
      </div>


    </div>
  )
}

export default Company