import React from 'react';

const MealList = ({ meals }) => (
    <ul>
        {meals.map((meal, index) => (
            <li key={index}>{meal}</li>
        ))}
    </ul>
);

export default MealList;
