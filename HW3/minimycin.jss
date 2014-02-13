(clear)
(mapclass Assertion)
(mapclass Identity)

(defrule R1 " "
	(and (object (is-a Assertion) 
	        (concept "immunosuppressed")
                (value TRUE))
		(object (is-a Assertion) 
	        (concept "TB_bacterimia")
                (value TRUE)))
 => (make-instance (str-cat Assertion (gensym*)) of Assertion
          (concept "disseminated_TB")(value TRUE))
)

(defrule R2 " "
	(object (is-a Assertion) 
	        (concept "urologic_manipulation")
                (value TRUE))
 => (make-instance (str-cat Assertion (gensym*)) of Assertion
          (concept "abnormal_urologic_anatomy")(value TRUE))
)

(defrule R3a " "
	(object (is-a Assertion)
		  (concept "catheterization")
		  (value TRUE))
=> (make-instance (str-cat Assertion (gensym*)) of Assertion
	(concept "urologic_manipulation")(value TRUE))
)

(defrule R3b " "
	(object (is-a Assertion) 
	        (concept "cytoscopy")
                (value TRUE))
 => (make-instance (str-cat Assertion (gensym*)) of Assertion
          (concept "urologic_manipulation")(value TRUE))
)

(defrule R4 " "
	(object (is-a Assertion) 
	        (concept "renal_abnormality")
                (value TRUE))
 => (make-instance (str-cat Assertion (gensym*)) of Assertion
          (concept "abnormal_urologic_anatomy")(value TRUE))
)

(defrule R5 " "
	(object (is-a Assertion) 
	        (concept "polycystic_kidneys")
                (value TRUE))
 => (make-instance (str-cat Assertion (gensym*)) of Assertion
          (concept "renal_abnormality")(value TRUE))
)

(defrule R6 " "
	(and (object (is-a Assertion) 
	        (concept "female")
                (value TRUE))
	     (object (is-a Assertion) 
	        (concept "adult")
                (value TRUE))
	     (object (is-a Assertion) 
	        (concept "dysuria")
                (value TRUE)))
 => (make-instance (str-cat Identity (gensym*)) of Identity
          (concept "E_Coli")(value TRUE))
)

(defrule R7 " "
	(and (object (is-a Assertion) 
	        (concept "immunosuppressed")
                (value TRUE))
	     (object (is-a Assertion) 
	        (concept "mycellia_in_urine")
                (value TRUE)))
 => (make-instance (str-cat Identity (gensym*)) of Identity
          (concept "fungus")(value TRUE))
)


(defrule R8b " "
	(object (is-a Assertion) 
	        (concept "chronic_steroids")
                (value TRUE))
 => (make-instance (str-cat Assertion (gensym*)) of Assertion
          (concept "immunosuppressed")(value TRUE))
)

(defrule R9 " "
	(and (object (is-a Assertion) 
	        (concept "urinary_tract_infection")
                (value TRUE))
	     (object (is-a Assertion) 
	        (concept "sterile_urine_culture")
                (value TRUE))
	     (object (is-a Assertion) 
	        (concept "disseminated_TB")
                (value TRUE)))
 => (make-instance (str-cat Identity (gensym*)) of Identity
          (concept "tubercile_baccilus")(value TRUE))
)

(defrule R10 " "
	(object (is-a Assertion) 
	        (concept "urinary_tract_infection")
                (value TRUE))
	(object (is-a Assertion) 
	        (concept "abnormal_urologic_anatomy")
                (value TRUE))
 => (make-instance (str-cat Identity (gensym*)) of Identity
          (concept "enterococcus")(value TRUE))
)

