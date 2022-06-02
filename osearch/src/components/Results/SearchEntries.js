import { useState,useEffect } from "react";
import { Link, useNavigate } from 'react-router-dom';

const SearchEntries = (props) => {
    const navigate = useNavigate()
    const handleClick = (link, company)=>{
        props.setCompany(company)
        navigate(link)
    }

        return(
            props.data.companies.map((company, index) => {
                props.setCompany(company)
                const link = "/"+company.company
                return (
                    <div key={index}>
                        <button onClick= {()=>{handleClick(link, company)}} >{company.company}</button>
                        {/* <Link to={{
                            pathname:link,
                            state:company
                        }}>
                            {company.company}
                        </Link> */}
                    </div>
                )
            })

        )

}

export default SearchEntries