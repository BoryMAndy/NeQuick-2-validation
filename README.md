# Testing ionospheric model NeQuick 2 using satellite measurements of electron density
**NeQuick** is a three-dimensional, time-dependent electron concentration model based on an empirical climatological representation of the ionosphere. It predicts monthly mean electron concentration using analytical profiles dependent on input parameters related to solar activity, such as sunspot numbers or solar flux, month, geographic latitude and longitude, altitude, and Universal Time (UT).  

To evaluate the modelling accuracy, direct electron concentration measurements obtained from **Langmuir probes** aboard the three **Swarm** satellites during the entirety of **2014** were used. To ensure accurate analysis, time periods are classified into **geomagnetic storm days** and **calm days**, using **Kp** and **AE indices**.  

This repository presents a methodology for verifying the **NeQuick 2** ionospheric model using **Swarm** satellite data. The validation process includes:  

✔ Model calculations  
✔ Error statistics analysis  
✔ Creation of spatial distribution maps for mean errors  
✔ Monthly mean error curves for various geomagnetic conditions and latitudinal zones  

---

## 📌 Methodology  

The analysis consists of two main scripts:  

1. **`raw_process.py`** – Performs direct model calculations and generates output files.  
2. **`map.ipynb`** – Processes data to create visualizations and spatial maps.  

---

## 📊 Examples of Code Application  

### **Spatial Distribution of Mean Annual Percentage Error**  
📍 *Mean annual percentage error of NeQuick 2 at 460 km altitude for 2014 (calm conditions).*  

<img src="https://github.com/user-attachments/assets/320c8695-d070-4e21-9d3d-e8fd73fa04c2" width="60%">  

---

### **Spatial Distribution of Mean Annual Percentage Error at the North Pole**  
📍 *Mean annual percentage error of NeQuick 2 at the North Pole (460 km altitude, 2014, calm conditions).*  

<img src="https://github.com/user-attachments/assets/c31c0aeb-c9dd-44bb-8eb1-2e80807c8bd5" width="60%">  

---

## 🔗 References  
1. Б. А. Матюшин, В. И. Захаров, Н. А. Сухарева, and О. В. Шестаков.  
   **Тестирование модели ионосферы NeQuick 2 на данных спутниковых измерений электронной концентрации.**  
   *Вестн. Моск. ун-та. Сер. 3. Физ. Астрон.* (2025), no. 1 (in Russian). 
2. [Conference Paper on Ionospheric Model Validation (2024)](http://conf.rse.geosmis.ru/thesisshow.aspx?page=293&thesis=10605)   
3. [ESA Data Portal](https://earth.esa.int/eogateway/catalog/swarm-ionosphere-magnetosphere)  
