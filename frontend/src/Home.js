import { Link } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";
import "./Home.css";
import rn1 from "./images/runner1.png";
import rn2 from "./images/runner2.png";
import rn3 from "./images/runner3.png";
import phone from "./images/phone contact.png";
import web from "./images/web contact.png";
import email from "./images/email contact.png";

export default function Home() {
  return (
    <section className="Home">
      <div className="bgHome"></div>
      <div className="info">
        <p>
          Here, photographers can easily upload their event photos, and
          participants can quickly find and view their personal marathon photos.
        </p>
        <div className="btngrp">
          <Link to="/Upload" className="btn1">
            <span>Upload</span>
          </Link>
          <Link to="/Search" className="btn1">
            <span>Search</span>
          </Link>
        </div>
        <div className="imggrp">
          <img src={rn1} alt="runner1" />
          <img src={rn2} alt="runner2" />
          <img src={rn3} alt="runner3" />
        </div>
      </div>
      <div className="contactus">
        <div className="contactuscenter">
          <h1>CONTACT US</h1>
        </div>
        <div className="contactusboxs">
          <div className="container">
            <div className="row">
              <div className="col-xl-4 col-lg-6	col-md-6 col-sm-12">
                <div className="contbox">
                  <img src={phone} alt="phone" />
                  <div className="continfo">
                    <h2>Phone</h2>
                    <h3>+212 6 21 79 74 90</h3>
                  </div>
                </div>
              </div>
              <div className="col-xl-4 col-lg-6 col-md-6 col-sm-12">
                <div className="contbox">
                  <img src={web} alt="web" />
                  <div className="continfo">
                    <h2>Website</h2>
                    <h3>www.MarathonPix.com</h3>
                  </div>
                </div>
              </div>
              <div className="col-xl-4 col-lg-12 col-md-12 col-sm-12">
                <div className="contbox" id="email123">
                  <img src={email} alt="email" />
                  <div className="continfo">
                    <h2>E-mail</h2>
                    <h3>MarathonPix@gmail.com</h3>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
