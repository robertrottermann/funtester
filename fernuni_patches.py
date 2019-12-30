# a very primitve way to patch up files
fernuni_patches = {
    "fsch_customer": [
        # filename, string to add
        (
            "security/ir.model.access.csv",
            "access_ir_module_category_manager,ir.module.category manager,base.model_ir_module_category,fsch_customer.group_fsch_manager,1,1,1,1",
        )
    ]
}
