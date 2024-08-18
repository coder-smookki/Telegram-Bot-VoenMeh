import React from "react";
import classes from "./Registration.module.scss"
import buttons from "../../sass/Buttons.module.scss"
import { useNavigate } from "react-router-dom";
import Gender from "./Gender.module.scss"
// Контейнер для содержимого страниц. Ограничивает его ширину.
const Container = ({ children }) => {
    let navigate = useNavigate()
    return <>
        <div className={classes.center}>
            <p className={classes.centered_text}>Теперь определимся с полом</p>
            <div className={Gender.ButtonsGender}>
					<button className={[buttons.btn, Gender.btn].join(" ")}>Мужской</button>
					<button className={[buttons.btn, Gender.btn].join(" ")}>Женский</button>
            </div>
        </div>
        <div className={classes.bottom}>
            <div className={classes.bottom_nav}>
                <button className={[buttons.btn, classes.btn].join(" ")} onClick={() => { navigate("/register/interesting") }}>Продолжить</button>
            </div>
        </div>
    </>;
};

export default Container;