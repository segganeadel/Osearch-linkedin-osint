import { useState,useEffect } from "react";
import { Link, useNavigate } from 'react-router-dom';

const SearchEntries = (props) => {
        return(
            props.data.results.map((company, index) => {
                const link = "/"+company.id
                return (
                    <div key={index}>
                        { <Link to={{
                            pathname:link,
                            query:{
                                active:props.active.a
                            }
                        }}>
                            {company.name}
                        </Link> }
                    </div>
                )
            })

        )

}

export default SearchEntries