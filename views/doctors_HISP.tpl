% rebase('layout.tpl', title='Home Page', year=year)

<div class="jumbotron">
    <h1>JogRX</h1>
	<h2>{{ title }}</h2>
	<h3>{{ message }}</h3>
	<form action="/doctors_HISP" method="post" class="form-horizontal" role="form">
    <div class="form-group">
      <div class="col-sm-7">
        HISP Address:<input name="hispAddress" id="email" placeholder="http://polaris.i3l.gatech.edu:8080/gt-fhir-webapp" required=True>
      </div> 
      <div class="col-sm-10">
        First Name: <input name="firstname" id="fname" placeholder="Clinton" required=True>
      </div>
      <div class="col-sm-10">
        Last Name: <input name="lastname" id="lname" placeholder="Gatech" required=True>
      </div>
      <div class="col-sm-10">
        Street Address: <input name="street" id="street" placeholder="x3129 Chilkat Court" required=True>
      </div>
      <div class="col-sm-10">
        Zip Code: <input name="postal" id="postal" placeholder="x30388" required=True>
      </div>
      <div class="col-sm-10">
        City: <input name="city" id="city" placeholder="xAtlanta" required=True>
      </div>
      <div class="col-sm-10">
        State: <select name="state" size="1">
          <option value="AL">Alabama</option>
          <option value="AK">Alaska</option>
          <option value="AZ">Arizona</option>
          <option value="AR">Arkansas</option>
          <option value="CA">California</option>
          <option value="CO">Colorado</option>
          <option value="CT">Connecticut</option>
          <option value="DE">Delaware</option>
          <option value="DC">Dist of Columbia</option>
          <option value="FL">Florida</option>
          <option value="GA">Georgia</option>
          <option value="HI">Hawaii</option>
          <option value="ID">Idaho</option>
          <option value="IL">Illinois</option>
          <option value="IN">Indiana</option>
          <option value="IA">Iowa</option>
          <option value="KS">Kansas</option>
          <option value="KY">Kentucky</option>
          <option value="LA">Louisiana</option>
          <option value="ME">Maine</option>
          <option value="MD">Maryland</option>
          <option value="MA">Massachusetts</option>
          <option value="MI">Michigan</option>
          <option value="MN">Minnesota</option>
          <option value="MS">Mississippi</option>
          <option value="MO">Missouri</option>
          <option value="MT">Montana</option>
          <option value="NE">Nebraska</option>
          <option value="NV">Nevada</option>
          <option value="NH">New Hampshire</option>
          <option value="NJ">New Jersey</option>
          <option value="NM">New Mexico</option>
          <option value="NY">New York</option>
          <option value="NC">North Carolina</option>
          <option value="ND">North Dakota</option>
          <option value="OH">Ohio</option>
          <option value="OK">Oklahoma</option>
          <option value="OR">Oregon</option>
          <option value="PA">Pennsylvania</option>
          <option value="RI">Rhode Island</option>
          <option value="SC">South Carolina</option>
          <option value="SD">South Dakota</option>
          <option value="TN">Tennessee</option>
          <option value="TX">Texas</option>
          <option value="UT">Utah</option>
          <option value="VT">Vermont</option>
          <option value="VA">Virginia</option>
          <option value="WA">Washington</option>
          <option value="WV">West Virginia</option>
          <option value="WI">Wisconsin</option>
          <option value="WY">Wyoming</option>
        </select>
      </div>
      <div class="col-sm-10">
        Sex: <input type="radio" name="sex" value="male" checked> Male
        <input type="radio" name="sex" value="female"> Female
      </div>
      <div class="col-sm-10">
        Date of Birth: <input type="date" name="birthdate" id="birthdate" placeholder="1999-12-02" required=True>
      </div>
    </div>
    <div class="form-group">
      <div class="col-sm-offset-2 col-sm-10">
        <input value="Submit" type="submit" class="btn btn-default active"/>
      </div>
    </div>
  </form>

</div>

