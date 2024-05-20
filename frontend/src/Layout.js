import React from 'react';
import { Link } from "react-router-dom";
import './Layout.css';
import logo from './images/Logo.png'


export default function Layout(){

    return(
        <header>
            <Link to="/"><img src={logo} alt="Logo"/></Link>
            <div className="list">
                <Link  to="/">HOME</Link>
                <Link  to="/Upload">UPLOAD</Link>
                <Link  to="/Search">SEARCH</Link>
            </div>
        </header>
    )
}
