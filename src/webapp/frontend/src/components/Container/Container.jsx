import React from "react";
import classes from "./Container.module.scss";

// Контейнер для содержимого страниц. Ограничивает его ширину.
const Container = ({ children }) => {
    return <div className={classes.main}>{children}</div>;
};

export default Container;