import React from 'react'
import './choose-set-page.styles.css'

import { LearningSetBox } from '../../components/learning-set-box/learning-set-box.component'
import Cookie from "js-cookie";
import axios from 'axios';

class ChooseSetPage extends React.Component {
    constructor(props){
        super(props);
    }

    render() {
        const token =  Cookie.get("token") ? Cookie.get("token") : null;
        console.log(token);
        
        axios.get(`http://127.0.0.1:8000/learning_sets/`)
        .then(res => {
            if (res.status === 200) {
                console.log(res.data);
            }
        })

        return (
            <div className="ChooseSetPage-container">
                <title className="ChooseSetPage-title">Choose learning set</title>

                <div className="ChooseSetPage-types">
                    <div className="ChooseSetPage-continue-column">
                        <h3 className="ChooseSetPage-continue">Continue</h3>
                        <div className="ChooseSetPage-box">
                            <LearningSetBox title_and_date={"Arbeit Wortschatz, from 21.04.2020"} progress={"67%"} />
                        </div>
                        <div className="ChooseSetPage-box">
                            <LearningSetBox title_and_date={"Arbeit Wortschatz, from 21.04.2020"} progress={"67%"} />
                        </div>

                    </div>

                    <div className="ChooseSetPage-begin-new-column">
                        <h3 className="ChooseSetPage-begin-new">Begin new</h3>

                        <div className="ChooseSetPage-begin-new-row">
                            <div className="ChooseSetPage-begin-new-wortschatz-column">
                                <h5 className="ChooseSetPage-wortschatz">Wortschatz</h5>
                                <div className="ChooseSetPage-box">
                                    <LearningSetBox title_and_date={"Arbeit Wortschatz"} />
                                </div>
                                <div className="ChooseSetPage-box">
                                    <LearningSetBox title_and_date={"Arbeit Wortschatz"} />
                                </div>
                            </div>

                            <div className="ChooseSetPage-begin-new-verb-rektion-column">
                                <h5 className="ChooseSetPage-verb-rektion">Verb Rektion</h5>
                                <div className="ChooseSetPage-box">
                                    <LearningSetBox title_and_date={"Arbeit Wortschatz"} />
                                </div>
                                <div className="ChooseSetPage-box">
                                    <LearningSetBox title_and_date={"Arbeit Wortschatz"} />
                                </div>
                            </div>
                        </div>
                    </div>


                </div>

            </div>

        )
    }
}

export { ChooseSetPage };