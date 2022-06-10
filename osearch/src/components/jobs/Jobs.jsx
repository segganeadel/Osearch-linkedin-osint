import "./Jobs.scss"

import React from 'react'

const Jobs = (props) => {
  const infos = props.data.jobs
  return (
    <div className="styled-table">
      <table>
        <tbody>
          {props.data.results.map((infos, index) => {
            return (
              <div key={index}>
                <tr>
                  <td>{infos.title}</td>
                  <td>{infos.link}</td>
                  <td>{infos.company}</td>
                  <td>{infos.adress}</td>
                  <td>{infos.date}</td>
                  <td>{infos.profile}</td>
                  <td>{infos.experience}</td>
                </tr>
              </div>)
          })
          }


        </tbody>
      </table>
    </div>
  )
}

export default Jobs

