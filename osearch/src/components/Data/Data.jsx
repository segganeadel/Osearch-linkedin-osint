import "./Data.css"


const Data = (props) => {
    const infos = props.data.company
    return (
        <div className="tableau_passive">
            <table>
                <tbody>
                    <tr>
                        <td>Nom de l'entreprise</td>
                        <td>{infos.companyname}</td>
                    </tr>
                    <tr>
                        <td>Taille de l'entreprise</td>
                        <td>{infos.size}</td>
                    </tr>
                    <tr>
                        <td>Siège social de l'entreprise</td>
                        <td>{infos.headquarters}</td>
                    </tr>
                    <tr>
                        <td>Adresse</td>
                        <td>{infos.address}</td>
                    </tr>
                    <tr>
                        <td>Adresse 2</td>
                        <td>{infos.address2}</td>
                    </tr>
                    <tr>
                        <td>Domaine</td>
                        <td>{infos.industries}</td>
                    </tr>
                    <tr>
                        <td>Spécialités</td>
                        <td>{infos.specialties}</td>
                    </tr>
                    <tr>
                        <td>Type de l'entreprise</td>
                        <td>{infos.type}</td>
                    </tr>
                    <tr>
                        <td>Fondée en </td>
                        <td>{infos.founded}</td>
                    </tr>
                    <tr>
                        <td>Siteweb</td>
                        <td>{infos.website}</td>
                    </tr>
                    <tr>
                        <td>Lien linkedin</td>
                        <td>{infos.url}</td>
                    </tr>
                    <tr>
                        <td>A propos</td>
                        <td>{infos.about}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    )

}

export default Data