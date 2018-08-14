odoo.define('realty_plan.dashboard', function(require){
"use strict";
    
var core = require('web.core');
var FormController = require('web.FormController');
var FormRenderer = require('web.FormRenderer');

var _t = core._t;
var QWeb = core.qweb;

FormController.include({
    /**
     * @override
     */
    getTitle: function () {
        if (this.inDashboard) {
            if(this.modelName == 'realty_plan.board'){
                return _t("My Realty Plan Dashboard");
            }else{
                return _t("My Dashboard");
            }
        }
        return this._super.apply(this, arguments);
    },
    /**
     * @private
     */
    _onEnableDashboard: function () {
        this.inDashboard = true;
        if(this.modelName == 'realty_plan.board'){
            this.defaultButtons = false;
        }
    },
});

FormRenderer.include({
    /**
     * @private
     * @param {object} node
     * @returns {jQueryElement}
     */
    _renderTagBoard: function (node) {
        var $html=this._super(node);
        if(this.state.model == "realty_plan.board"){
            $html.find(".oe_dashboard_links").remove();
            $html.find(".oe_action .oe_icon").remove();
            $html.find(".oe_dashboard_column").unbind("sortstop");
        }
        return $html;
    },
});


});
