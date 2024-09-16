import React from 'react'

const Tile = ({title, author, url, score, time}) => {
  return (
    <div className="tile">
        <h2><a href={`${url}`}>{title}</a></h2>
        <h4>By: {author}</h4>
        <div className="line2">
            <span>{time}</span>
            <span>Score: <strong>{score}</strong></span>
        </div>
    </div>
  )
}

export default Tile