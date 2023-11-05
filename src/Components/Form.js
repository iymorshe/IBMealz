import React, { useState } from 'react';

function TextBox() {
    const [cuisine, setMealPreference] = useState('');
    // const [soupOrSalad, setSoupOrSalad] = useState('');
    // const [riceOrBeans, setRiceOrBeans] = useState('');
    // const [chickenOrBeef, setChickenOrBeef] = useState('');
    // const [coldOrHot, setColdOrHot] = useState('');

    const handleMealPreferenceChange = (event) => {
        setMealPreference(event.target.value);
    };

    // const handleSoupOrSaladChange = (event) => {
    //     setSoupOrSalad(event.target.value);
    // };

    // const handleRiceOrBeansChange = (event) => {
    //     setRiceOrBeans(event.target.value);
    // };

    // const handleChickenOrBeefChange = (event) => {
    //     setChickenOrBeef(event.target.value);
    // };

    // const handleColdOrHotChange = (event) => {
    //     setColdOrHot(event.target.value);
    // };

    const handleSubmit = (event) => {
        event.preventDefault();
        const location = event.target.location.value;
        const userPreferences = event.target.userPreferences.value;
        const data = { location, cuisine, userPreferences};
        console.log(data);
        fetch('http://localhost:5000/food_input', {
            method: 'POST',
            mode: 'no-cors',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch((error) => {
            console.error('Error:', error);
        });
    };

    return (
        <div>
            <h2>Please input your preferences</h2>
            <form onSubmit={handleSubmit}>
                <div>
                <label>
                    Your Location:     
                    <input type="text" name="location" />
                </label>
                </div>
                <br />
                <div>
                <label>
                    userPreferences:     
                    <input type="text" name="userPreferences" />
                </label>
                </div>
                <br />
                <div>
                <label>
                    Meal Preferences:
                    <select value={cuisine} onChange={handleMealPreferenceChange} name="cuisine">
                        <option value="">Select an option</option>
                        <option value="Halal">Halal</option>
                        <option value="Vegan">Vegan</option>
                        <option value="Vegetarian">Vegetarian</option>
                        <option value="Anything">Anything</option>
                    </select>
                </label>
                </div>
                <br />
                {/* <div>
                <label>
                    Soup or Salad:
                    <select value={soupOrSalad} onChange={handleSoupOrSaladChange} name="soupOrSalad">
                        <option value="">Select an option</option>
                        <option value="Soup">Soup</option>
                        <option value="Salad">Salad</option>
                    </select>
                </label>
                </div>
                <br />
                <div>
                <label>
                    Rice or Beans:
                    <select value={riceOrBeans} onChange={handleRiceOrBeansChange} name="riceOrBeans">
                        <option value="">Select an option</option>
                        <option value="Rice">Rice</option>
                        <option value="Beans">Beans</option>
                    </select>
                </label>
                </div>
                <br />
                <div>
                <label>
                    Chicken or Beef:
                    <select value={chickenOrBeef} onChange={handleChickenOrBeefChange} name="chickenOrBeef">
                        <option value="">Select an option</option>
                        <option value="Chicken">Chicken</option>
                        <option value="Beef">Beef</option>
                    </select>
                </label>
                </div>
                <br />
                <div>
                <label>
                    Cold or Hot:
                    <select value={coldOrHot} onChange={handleColdOrHotChange} name="coldOrHot">
                        <option value="">Select an option</option>
                        <option value="Cold">Cold</option>
                        <option value="Hot">Hot</option>
                    </select>
                </label>
                </div>
                <br /> */}
                <input type="submit" value="Submit" />
            </form>
        </div>
    );
}

export default TextBox;
