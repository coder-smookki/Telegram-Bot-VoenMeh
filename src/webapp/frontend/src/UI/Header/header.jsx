import React from "react";
import classes from "./Header.module.scss";
import Back from '../../assets/back.svg';
function Header() {
  return (
    <>
      <div className={classes.header}>
        <div className={classes.header_nav}>
          <img src={Back}/>
          <p className={classes.title}>Ньютончик</p>
        </div>
      </div>
    </>
  )
}

export default Header
