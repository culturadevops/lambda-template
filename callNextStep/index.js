var AWS = require('aws-sdk');
AWS.config.update({region: 'us-east-1'});
var Lambda = new AWS.Lambda();

var NEXT_STEP_API = process.env.NEXT_STEP_API;

function callNextStep(){
  if (NEXT_STEP_API !== null && NEXT_STEP_API !== undefined) {
      console.log('invoking lambda', NEXT_STEP_API);
      Lambda.invoke({
          FunctionName: NEXT_STEP_API,
          InvocationType: "Event"
      }, function(e, d) {
          if (e) {
              console.error("invocation error", JSON.stringify(e));
          } else {
              console.log("invocation success", d);
          }
      });
  }             
}

exports.handler = (event, context, callback) => {
  context.callbackWaitsForEmptyEventLoop = false;
  callNextStep();

};