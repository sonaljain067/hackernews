import axios from "axios";
import { useEffect, useState } from 'react';
import './App.css';
import Tile from './Tile';
// import { SkeletonLoader } from "./Loader";

const SkeletonLoader = ({ length = 15 }) => {
  const skeletons = Array.from({ length }, (_, idx) =>  <div key 
={idx} className="skeleton-shape"></div>)
  return <div className="skeleton-loader">
    {skeletons}
  </div>
}

function App() {
  const [stories, setStories] = useState([]); 
  const [error, setError] = useState(""); 

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/")
      .then(response => setStories(response.data))
      .catch(err => {
        console.log(err.response.data.detail)
        setError(err.response.data.detail)
      })
  }, [])

  return (
    <div className="app">

      <h1>Top News</h1>
      {error && stories.length === 0 && <div className="red">{error}</div>}
      {!error && stories.length === 0 && <SkeletonLoader />}

      <div className="content">
        {stories && stories.map(story => 
          <Tile title={story.title} author={story.author} url={story.url} score={story.score} time={story.time} key={story.time}/>  
        )}
      </div>

    </div>
  );
}

export default App;
