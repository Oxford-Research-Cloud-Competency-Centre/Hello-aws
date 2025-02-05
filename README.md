© The Chancellor, Masters and Scholars of The University of Oxford. All rights reserved.

# Explore different providers

This course is available for multiple cloud providers. Choose your preferred platform:

- [Hello Google Cloud](https://github.com/Oxford-Research-Cloud-Competency-Centre/Hello-gcloud)
- [Hello Microsoft Azure](https://github.com/Oxford-Research-Cloud-Competency-Centre/Hello-mazure)
- [Hello Amazon Web Services](https://github.com/Oxford-Research-Cloud-Competency-Centre/Hello-aws) (⭐ Most popular)
- Hello Oracle Cloud *(Coming Soon)*

*Note: Entries marked with "Coming Soon" are planned versions that are currently under development.*

# Instructions

<details>
<summary>Step 1. Fork (or make a copy of) this repository</summary>

![Step 2](README_images/download.png)

***
</details>
<details>
<summary>Step 2. Go to the AWS Console and type "app runner" in the search bar</summary>

![Step 2](README_images/img1.png)

***
</details>
<details>
<summary>Step 3. Create a new service</summary>

![Step 3](README_images/img2.png)

***
</details>
<details>
<summary>Step 4. Select source code repository and link your repository</summary>

![Step 4](README_images/img3.png)

***
</details>
<details>
<summary>Step 5. Set deployment to automatic</summary>

![Step 5](README_images/img4.png)

***
</details>
<details>
<summary>Step 6. Select "Use a configuration file" (apprunner.yaml is already in the repository)</summary>

![Step 6](README_images/img5.png)

***
</details>

<details>
<summary>Step 7. Choose a name for your service and deploy it. Default settings like 1 CPU and 2 GB RAM are enough.</summary>

![Step 7](README_images/img6.png)

***
</details>

Voilà! Access the URL.

![Voilà](README_images/img7.png)

***

# Going further

<details>
<summary><h2>Modifying the code</h2></summary>

<details>
<summary>You can commit some changes to your repository and watch how the service is updated automatically.</summary>

![Updating a service](README_images/update.png)
</details>
</details>

<details>
<summary><h2>Using a custom domain</h2></summary>

<details>
<summary>Step 1. If you want to use a custom domain (like hello.com), just click "Link domain".</summary>

![Linking the domain](README_images/link_domain.png)

***
</details>
<details>
<summary>Step 2. If you are using Route 53, then AWS should create the record for you. You don't need to do this step but you might need to delete the records manually when you remove the service.</summary>


![The DNS record](README_images/domain_routing.png)

***
</details>
Voilà! 

![Voilà](README_images/domain.png)

</details>

<details>
<summary><h2>Cleaning up</h2></summary>

<details>
<summary>Don't forget to delete your service when you are no longer using it. You can always redeploy later. </summary>

![Deleting a service](README_images/delete.png)
</details>

</details>

<details>
<summary><h2>Adding an API endpoint</h2></summary>

<details>
<summary>Add the following code in app.py</summary>

```	
@app.route("/hello_api")
def hello_api():
    return {
		"name": "Wrinkle Five Star",
		"species": "Duck",
		"breed": "American Pekin",
		"hatching_date": "2020-09-09",
		"sex": "Male"
    }
```
</details>

Then test your endpoint

![API endpoint](README_images/hello_api.png)

</details>

<details>
<summary><h2>User interface</h2></summary>

<details>
<summary>...</summary>
Missing content
</details>

</details>

<details>
<summary><h2>Database writing/reading</h2></summary>

<details>
<summary>Go to the AWS Console and type "RDS" in the search bar</summary>
Missing content
</details>

</details>

<details>
<summary><h2>Storage bucket writing/reading</h2></summary>

<details>
<summary>Go to the AWS Console and type "S3" in the search bar</summary>
Missing content
</details>

</details>

<details>
<summary><h2>Local testing</h2></summary>

After a while, it's not fun anymore to wait for deployment. You want to test your changes before. 

<details>
<summary>Step 1. Install git and clone the repository on your local machine</summary>

```	
	git clone {repository_link}
```

***
</details>
<details>
<summary>Step 2. Install Python</summary>

```	
https://www.python.org/downloads/
```

***
</details>
<details>
<summary>Step 3. Install dependencies</summary>

```	
	 py -m pip install flask
```

***
</details>
<details>
<summary>Step 4. Run flask</summary>

```	
	 py -m flask run
```

Open localhost:5000 in your browser.  

***
</details>

![Local testing](README_images/local_testing.png)

</details>


