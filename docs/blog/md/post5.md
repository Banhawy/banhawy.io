
# Switching to HTTPS for Sites Hosted on AWS 

Since [Google's push](https://serverguy.com/security/google-forcing-ssl-certificate-websites/) towards a more secure web and required SSL Certificates for websites to avoid being flagged as unsafe, having your website support HTTPS connections is a must.

If your hosting your business or personal website on Amazon's AWS like me, you might have noticed that Amazon only allows http connection to your domain by default via [Amazon CloudFront](https://aws.amazon.com/cloudfront/). You are also given an SSL certificate that allows HTTPS connections. However, that would require using a different URL that uses the default CloudFront Certificate and ends in *.cloudfront.net*.

If you want your users to use HTTPS and you want to use your own domain name in the URLs for your objects (for example, https://www.example.com/image.jpg), you need to perform several additional steps.

## Who Should Use this Guide 
There are many ways you can obtain an SSL certificate. In this post, I will only discuss how to get one using **AWS Certificate Manager(ACM)**. You should continue reading if:
1. You have a website/webapp hosted on [AWS](https://aws.amazon.com/websites/).
2. You use [Amazon Route 53](https://aws.amazon.com/route53/) to manage your domain name.
3. You use [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html) to deliver your content.

### Step 1:  Check your Current Certificates 
 To begin with, check what certificates you already have. Go to the [AWS CloudFront Manager](https://console.aws.amazon.com/cloudfront/home) and go to the *Distributions* page and click on your site's ID. Next, make sure you're on the *General* tab and click **Edit**. This will show you your website's distribution settings. By default you should see that your SSL Certificate is set to the *Default CloudFront Certificate*. 

 ![Check Certificate](../img/aws-1.png) 

 ### Step 2: Request a Certificate with ACM
 
 Since you want your own custom SSL certificate, you should click on **Request or Import a Certificate with ACM**. This will redirect you to the *AWS Certificate Manager* where you can request the certificate. 

 ![Request Domain Name](../img/aws-2.png)

 Add your domain name on the first screen and click Next. You have the option to use an asterix (\\*) as a wild card before your domain name to secure other sites on your domain.
 If you're going with the wildcard option, make sure you add **both** your base domain name (*example.com*) and the wildcard format (\\*.example.com).


 ![Request Domain Name](../img/aws-3.png)

 Next, select **DNS validation** as the validation method. This is generally faster than email and can be handled by Amazon Route 53 for you.

 ![Request Domain Name](../img/aws-3.1.png)
 
 On the next screen, review the information you provided for your request,and choose **Confirm and request**. The following page shows that your request status is pending validation.

 ![Request Domain Name](../img/aws-4.png)

If all goes well, the following page will show that your request is pending validation. Come back to that page to check your request status.

**Note: After AWS issues the certificate, ACM changes the certificate status to *Issued*. You can continue with the next steps without waiting. However, the desired outcome won't happen without the issuing the certificate.

### Step 3: Update CloudFront Distribution
Similar to step 1, go to the [AWS CloudFront Manager](https://console.aws.amazon.com/cloudfront/home) and open your site's distributions settings. Click Edit in the **General** tab.

Choose *Custom SSL Certificate* and select your certificate from the dropdown list. Click **Yes, Edit**.

### Step 4: Configure CloudFront to require HTTPS between viewers and CloudFront

On the **Behaviors** tab, choose the cache behavior that you want to update, and choose Edit.


 ![Viewer Protocol Policy](../img/aws-6.png)

For the **Viewer Protocol Policy**, choose one of these options:

- **Redirect HTTP to HTTPS**
Viewers can use both protocols, but HTTP requests are automatically redirected to HTTPS requests. CloudFront returns HTTP status code 301 (Moved Permanently) along with the new HTTPS URL. The viewer then resubmits the request to CloudFront using the HTTPS URL.

    When a viewer makes an HTTP request that is redirected to an HTTPS request, CloudFront charges for both requests. For the HTTP request, the charge is only for the request and for the headers that CloudFront returns to the viewer. For the HTTPS request, the charge is for the request, and for the headers and the object returned by your origin.

- **HTTPS Only**
Viewers can access your content only if they're using HTTPS. If a viewer sends an HTTP request instead of an HTTPS request, CloudFront returns HTTP status code 403 (Forbidden) and does not return the object.

When done, click **Yes, Edit**.

Now all you have to do is to wait for Amazon Route 53 to associate the new domain SSL certificate with your website which might take 15-60 minutes.

For more detailed documentation on how Amazon CloudFront works see [this link](https://aws.amazon.com/documentation/cloudfront/). 

For detailed documentation on how Amazon Route 53 works, see [this link.](https://aws.amazon.com/documentation/acm/)