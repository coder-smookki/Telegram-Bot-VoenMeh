import React from "react";
import classes from "./App.module.scss";

// Контейнер для содержимого страниц. Ограничивает его ширину.
const App = ({ children }) => {
    return <div className={classes.app}>{children}</div>;
};

export default App;