import React from "react";
import classes from "./Registration.module.scss"
import buttons from "../../sass/Buttons.module.scss"
import { useNavigate } from "react-router-dom";
// Контейнер для содержимого страниц. Ограничивает его ширину.
const Container = ({ children }) => {
    let navigate = useNavigate()
    return <>
        <div className={classes.center}>
            <p className={classes.centered_text}>Сколько тебе лет?</p>
        </div>
        <div className={classes.bottom}>
            <div className={classes.bottom_nav}>
                <button className={[buttons.btn, classes.btn].join(" ")} onClick={() => { navigate("/register/gender") }}>Продолжить</button>
            </div>
        </div>
    </>;
};

export default Container;