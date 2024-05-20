import React, { useEffect, useState } from "react";
import "./Search.css";

const Search = () => {
  const [imageArray, setImageArray] = useState([]);
  const [searchInput, setSearchInput] = useState("");

  const backend = "http://localhost:8000/";

  const getImage = () => {
    fetch(backend + "number" + "?bib_number=" + searchInput)
      .then((res) => {
        if (!res.ok) {
          throw new Error("Network response was not ok");
        }
        console.log(res);
        return res.json();
      })
      .then((json) => {
        setImageArray(json);
      });
  };

  useEffect(() => {
    getImage();
  }, [searchInput]);

  const handleSearch = (e) => {
    e.preventDefault();
    const searchValue = document.querySelector("#search").value;
    setSearchInput(searchValue);
  };
  // let imagefilter = null;
  // if (imageList != null) {
  //   arrayImage = Object.entries(imageList);
  //   imagefilter = arrayImage.filter((objet) => {
  //     return objet[0] === searchInput;
  //   });
  // }

  return (
    // <section className='Searchpage'>
    // <form className='bib'>
    //     <input type="text" id="search"/>
    //     <button type="submit"  onClick={(e)=>handleSearch(e)}>search</button>
    //   </form>
    //   {console.log(arrayImage)}
    //   <div> {arrayImage!=null?imagefilter.map((object,key)=><li key={key}>{object[1].map((obj,key)=><img src={obj} key={key} alt='err'></img>)} </li>):''}</div>
    // </section>
    <section className="Searchpage container-fluid">
      <form className="bib mb-4" onSubmit={handleSearch}>
        <div className="input-group">
          <input
            type="text"
            id="search"
            className="form-control"
            placeholder="Enter bib number"
          />
          <button type="submit" className="btn btn-gray">
            Search
          </button>
        </div>
      </form>
      {console.log(imageArray)}
      <div className="row overflow-auto">
        {imageArray !== null ? (
          imageArray.map((imagePath, idx) => (
            <div key={idx} className="col-md-4 col-sm-6 mb-3">
              <img
                src={backend + imagePath}
                className="img-fluid rounded img-thumbnail"
                alt="Img"
              />
            </div>
          ))
        ) : (
          <p>No images found.</p>
        )}
      </div>
    </section>
  );
};

export default Search;
