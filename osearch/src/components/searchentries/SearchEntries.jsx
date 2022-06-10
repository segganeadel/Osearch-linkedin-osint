import "./SeachEntries.scss"
import { Link } from 'react-router-dom';

const SearchEntries = (props) => {




    return (
        <div>
            <div className="titre">
                Resultats :
            </div>
            {props.data.results.map((company, index) => {
                const link = "/" + company.id
                return (
                    <div key={index}>
                        <div className="result">
                            <Link to={{ pathname: link, }}>{company.name}</Link>
                            <div className="desc"><span>{company.desc}</span></div>
                        </div>
                    </div>
                )
            })
            }
        </div>


    )

}

export default SearchEntries