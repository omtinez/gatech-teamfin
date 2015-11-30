% rebase('layout.tpl', title='Display Data', year=year)
<div class="jumbotron">
	<form  action="/displayData" method="post" class="form-horizontal" role="form">
	<div class="form-group pull-right">
      <div class="col-sm-offset-2 col-sm-10" >
        <!-- <input value="Current Progress"  type="submit" name="Accept" class="btn btn-primary active"/> -->
      </div>
    </div>
	</form>
    <h3>FHIR User Observation</h3>

    <pre style="border-left: medium solid; padding-left: 1em; display:table">{{observations_raw}}</pre>

</div>
