from odoo import fields, models


class MrpWorkorderInherit(models.Model):
    _inherit = 'mrp.workorder'

    production_product_id = fields.Many2one(related='production_id.product_id', string="Product")
    production_date_planned = fields.Datetime(related='production_id.date_planned_start', string="Schedule Date")
    production_bom_id = fields.Many2one(related='production_id.bom_id', string="Bill of Material")
    production_user_id = fields.Many2one(related='production_id.user_id', string="Responsible")

    production_x_studio_film_width_mm = fields.Integer(related='production_id.x_studio_film_width_mm',
                                                       string="Film Width (mm)")
    production_x_studio_film_gusset_mm = fields.Integer(related='production_id.x_studio_film_gusset_mm',
                                                        string="Film Gusset (mm)")
    production_x_studio_bag_width_mm = fields.Integer(related='production_id.x_studio_bag_width_mm',
                                                      string="Bag Width (mm)")
    production_x_studio_bag_length_mm = fields.Integer(related='production_id.x_studio_bag_length_mm',
                                                       string="Bag Length (mm)")
    production_x_studio_film_gauge_um = fields.Integer(related='production_id.x_studio_film_gauge_um',
                                                       string="Film Gauge (um)")
    production_x_studio_film_colour = fields.Selection(related='production_id.x_studio_film_colour',
                                                       string="Film Colour")
    production_x_studio_tint = fields.Boolean(related='production_id.x_studio_tint',
                                              string="Tint")
    production_x_studio_special_instructions = fields.Html(related='production_id.x_studio_special_instructions')
    production_x_studio_length_per_roll_m = fields.Float(related='production_id.x_studio_length_per_roll_m')
    production_x_studio_kg_per_1000_bags = fields.Float(related='production_id.x_studio_kg_per_1000_bags')
    production_x_studio_desired_film_qty = fields.Integer(related='production_id.x_studio_desired_film_qty')
    production_x_studio_qty_bags_to_produce = fields.Float(related='production_id.x_studio_qty_bags_to_produce')
    x_studio_qty_bags_to_produce = fields.Float(related='production_id.x_studio_qty_bags_to_produce')
    production_x_studio_extrusion_speed = fields.Float(related='production_id.x_studio_extrusion_speed')
    production_x_studio_line_speed = fields.Float(related='production_id.x_studio_line_speed')
    production_x_studio_air_speed = fields.Float(related='production_id.x_studio_air_speed')
    production_x_studio_outputhr = fields.Float(related='production_id.x_studio_outputhr')
    production_x_studio_printing_plate = fields.Binary(related='production_id.x_studio_printing_plate')
    production_x_studio_printing_colour = fields.Selection(related='production_id.x_studio_printing_colour')
    production_x_studio_treatment = fields.Selection(related='production_id.x_studio_treatment')
    production_x_studio_top_temperature = fields.Float(related='production_id.x_studio_top_temperature')
    production_x_studio_bottom_temp = fields.Float(related='production_id.x_studio_bottom_temp')
    production_x_studio_machine_speed = fields.Float(related='production_id.x_studio_machine_speed')
    production_x_studio_belt_speed = fields.Float(related='production_id.x_studio_belt_speed')
    production_x_studio_client = fields.Char(related='production_id.x_studio_client')
    production_x_studio_po = fields.Char(related='production_id.x_studio_po')
    production_x_studio_roll_weight_kg = fields.Integer(related='production_id.x_studio_roll_weight_kg')
    production_x_studio_total_rolls_to_produce = fields.Float(related='production_id.x_studio_total_rolls_to_produce')
    production_x_studio_total_order_quantity = fields.Float(related='production_id.x_studio_total_order_quantity')
    production_x_studio_bags_per_roll_or_crt = fields.Integer(related='production_id.x_studio_bags_per_roll_or_crt')