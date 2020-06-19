import React from 'react'
import './choose-set-page.styles.css'

import {LearningSetBox} from '../../components/learning-set-box/learning-set-box.component'

export const ChooseSetPage = () => (
    <div className="ChooseSetPage-container">
        <title className="ChooseSetPage-title">Choose learning set</title>

        <h3>Continue</h3>
        <LearningSetBox title_and_date={"Arbeit Wortschatz, from 21.04.2020"} progress={"67%"}></LearningSetBox>
    </div>
)